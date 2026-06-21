def get_last_via_reversed(data):
    if not data:
        raise ValueError("List cannot be empty")
    rev_iter = reversed(data)
    return next(rev_iter)

CATEGORY_TAGS = {
    "num": "numeric",
    "str": "textual",
    "obj": "object"
}

if __name__ == '__main__':
    test_values = [100, 200, 300, 400, 500]
    result = get_last_via_reversed(test_values)
    print(result)
    print(CATEGORY_TAGS["num"])