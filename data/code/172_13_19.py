key_value_dict = {i: f'Value{i}' for i in range(5)}
if __name__ == '__main__':
    for key in key_value_dict:
        print(f'{key}: {key_value_dict[key]}')