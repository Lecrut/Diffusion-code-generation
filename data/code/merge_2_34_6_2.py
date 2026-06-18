import json
import sys
def main():
    data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 87},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
    for item in data:
        print(json.dumps(item))
if __name__ == '__main__':
    main()