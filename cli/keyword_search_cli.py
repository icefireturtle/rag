import argparse
import json

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()
    results = []

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            with open('data/movies.json', 'r') as file:
                data = json.load(file)
                movies = data['movies']
                for movie in movies:
                    if len(results) == 5: 
                        break
                    if args.query in movie['title']:
                        results.append(movie)
        case _:
            parser.print_help()

    if results: 
        for i in range(len(results)):
            print(f"{i+1}. {results[i]['title']}")

if __name__ == "__main__":
    main()