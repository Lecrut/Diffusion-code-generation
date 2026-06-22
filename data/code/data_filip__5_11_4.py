def title_case_tuple(input_tuple):
    return tuple(word.capitalize() for word in input_tuple)

if __name__ == '__main__':
    sample_data = ("hElLo", "WoRlD", "PyThOn")
    result = title_case_tuple(sample_data)
    print(result)