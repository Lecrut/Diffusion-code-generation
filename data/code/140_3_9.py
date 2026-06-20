def is_temp_safe(temp):
    return 15 <= temp <= 30

if __name__ == '__main__':
    sample_temp = 25
    output = is_temp_safe(sample_temp)
    print(output)