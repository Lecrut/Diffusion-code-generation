def get_third_element_negative_index(data):
    try:
        return data[-3]
    except TypeError:
        raise TypeError("Input must be a sequence")
    except IndexError:
        raise IndexError("Sequence must have at least three elements")

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400, 500]
    result = get_third_element_negative_index(sample_values)
    print(result)