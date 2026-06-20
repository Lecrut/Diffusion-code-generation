def compare_lengths(length1, length2):
    if length1 > length2:
        return {"length1": True, "length2": False}
    elif length2 > length1:
        return {"length1": False, "length2": True}
    else:
        return {"length1": None, "length2": None}

if __name__ == '__main__':
    result = compare_lengths(10, 20)
    print(result)