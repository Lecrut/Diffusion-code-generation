def get_first_element(integers: list[int]) -> int:
    return integers[0]

if __name__ == '__main__':
    sample_list = [42, 17, 29, 8]
    result = get_first_element(sample_list)
    print(result)