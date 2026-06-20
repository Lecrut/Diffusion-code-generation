def get_opposite(value_str):
    if value_str.lower() == 'true':
        return 'False'
    elif value_str.lower() == 'false':
        return 'True'
    else:
        raise ValueError("Invalid boolean string")

if __name__ == '__main__':
    sample1 = 'True'
    opposite1 = get_opposite(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    
    sample2 = 'false'
    opposite2 = get_opposite(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")