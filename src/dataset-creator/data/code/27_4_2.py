from collections import Counter
import functools
def sort_fruits(fruit_counts: dict) -> list[str]:
    sorted_items = sorted(
        fruit_counts.items(),
        key=lambda x: (x[0], -x[1])
    )
    return [name for name, _ in sorted_items]
if __name__ == '__main__':
    sample_data = {
        "apple": 5,
        "banana": 3,
        "cherry": 7,
        "date": 2,
        "elderberry": 4,
        "fig": 6,
        "grape": 8
    }
    sorted_fruits = sort_fruits(sample_data)
    print(sorted_fruits)