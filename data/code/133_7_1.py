def string_list_to_bool_list(str_list):
    bool_list = []
    for s in str_list:
        if s == 'True':
            bool_list.append(True)
        elif s == 'False':
            bool_list.append(False)
        else:
            raise ValueError(f"Unexpected string encountered: {s}")
    return bool_list
if __name__ == '__main__':
    sample_input = ['True', 'False', 'True', 'False']
    result = string_list_to_bool_list(sample_input)
    print(result)