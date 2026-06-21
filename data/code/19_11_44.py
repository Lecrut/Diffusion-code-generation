def is_special_float(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    test_data = {
        'pi': 3.14,
        'not_pi_int': 3,
        'not_pi_str': '3.14',
        'close_to_pi': 3.1400000000000001,
        'pi_float': float('3.14')
    }
    
    for key, value in test_data.items():
        result = is_special_float(value)
        print(f"{key}: {result}")