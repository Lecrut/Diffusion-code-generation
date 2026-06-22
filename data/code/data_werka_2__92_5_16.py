def yield_opposite_bools(data):
    result = []
    for element in data:
        if element is True:
            result.append(False)
        elif element is False:
            result.append(True)
        else:
            raise ValueError(f"Expected bool, got {type(element)}")
    for item in result:
        yield item

if __name__ == '__main__':
    input_list = [True, True, False, False, True]
    inverted = list(yield_opposite_bools(input_list))
    print(inverted)