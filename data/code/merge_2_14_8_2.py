import sys
def remove_duplicates(items):
    seen = {}
    result = []
    for item in items:
        if id(item) not in seen:
            seen[id(item)] = True
            result.append(item)
    return result
if __name__ == '__main__':
    data = [1, 2.0, "a", (3,), {"key": "val"}, [4], 5, 6]
    cleaned_data = remove_duplicates(data)
    print(cleaned_data)