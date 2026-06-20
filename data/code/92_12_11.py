def get_opposite(value):
    if value.lower() == 'true':
        return 'False'
    elif value.lower() == 'false':
        return 'True'
    else:
        raise ValueError("Input must be a valid boolean string ('True' or 'False')")

if __name__ == '__main__':
    sample1 = 'True'
    opposite1 = get_opposite(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    sample2 = 'false'
    opposite2 = get_opposite(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")