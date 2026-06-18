def verify_nested_equality(nested_list):
    return all(item == "target" for item in nested_list)
if __name__ == '__main__':
    sample_data = [["a", "b"], ["c", "d"]]
    result1 = all(x == "a" for x in sample_data[0])
    result2 = all(y == "c" for y in sample_data[1])
    print(f"All elements in first sub-list equal to target: {result1}")
    print(f"All elements in second sub-list equal to target: {result2}")