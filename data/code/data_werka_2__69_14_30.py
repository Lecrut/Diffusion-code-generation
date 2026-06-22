def access_elements_by_index(sample_list):
    if not isinstance(sample_list, list):
        raise ValueError("Input must be a list")
    for index in range(len(sample_list)):
        try:
            print(sample_list[index])
        except IndexError as e:
            print(f"IndexError: {e}")

if __name__ == '__main__':
    sample_values = [500, 600, 700, 800, 900]
    access_elements_by_index(sample_values)