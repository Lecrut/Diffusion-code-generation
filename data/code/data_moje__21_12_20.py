def greatest_of_three(x1, x2, x3):
    def is_greatest(candidate, other1, other2):
        return candidate >= other1 and candidate >= other2
    
    if is_greatest(x1, x2, x3):
        return x1
    if is_greatest(x2, x1, x3):
        return x2
    return x3

if __name__ == '__main__':
    value1 = 10
    value2 = 25
    value3 = 15
    final_result = greatest_of_three(value1, value2, value3)
    print(final_result)