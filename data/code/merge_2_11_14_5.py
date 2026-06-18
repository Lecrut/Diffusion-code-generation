import sys
def find_duplicates(data):
    seen = set()
    duplicates = []
    for item in data:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10 + [1, 2, 3]
    dupes = find_duplicates(sample_data)
    print(f"Duplicate values found: {dupes}")