CATEGORY_LOOKUP = {
    "odd": "Middle of odd length list",
    "even": "Middle of even length list"
}

def get_central_element(data):
    if not data:
        raise IndexError("Cannot access central element of an empty list")
    index = len(data) // 2
    return data[index]

if __name__ == '__main__':
    test_cases = [
        [5, 10, 15, 20, 25],
        [2, 4, 6, 8],
        [42],
        ["a", "b", "c", "d", "e", "f"]
    ]
    for case in test_cases:
        result = get_central_element(case)
        list_type = "odd" if len(case) % 2 != 0 else "even"
        print(f"{CATEGORY_LOOKUP[list_type]}: {result}")