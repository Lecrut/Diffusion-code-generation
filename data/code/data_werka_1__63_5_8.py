def get_first_item(mixed_list):
    if mixed_list:
        return mixed_list[0]
    else:
        return None

if __name__ == '__main__':
    sample_values = [42, 'hello', 3.14, True, None]
    print(get_first_item(sample_values))