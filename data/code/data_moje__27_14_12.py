def validate_triangle(s1, s2, s3):
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        return False
    if s1 + s2 <= s3:
        return False
    if s1 + s3 <= s2:
        return False
    if s2 + s3 <= s1:
        return False
    return True

if __name__ == '__main__':
    result = validate_triangle(3, 4, 5)
    print(result)
    
    result_invalid = validate_triangle(1, 2, 3)
    print(result_invalid)
    
    result_negative = validate_triangle(-1, 4, 5)
    print(result_negative)