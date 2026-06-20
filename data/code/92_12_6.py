def get_opposite(value):
    return not value

if __name__ == '__main__':
    sample1 = 'True'
    opposite1 = get_opposite(sample1.lower() == 'true')
    print(f"Original: {sample1}, Opposite: {opposite1}")
    
    sample2 = 'False'
    opposite2 = get_opposite(sample2.lower() == 'true')
    print(f"Original: {sample2}, Opposite: {opposite2}")