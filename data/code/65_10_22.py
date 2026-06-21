def fetch_sublist(input_list):
    try:
        return input_list[2:5]
    except TypeError as e:
        raise ValueError("Input must be a list") from e

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55, 65]
    extracted_sublist = fetch_sublist(sample_data)
    print(extracted_sublist)