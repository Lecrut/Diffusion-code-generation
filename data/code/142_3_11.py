BOOL_TRUE = True
BOOL_FALSE = False

def compare_booleans(a, b):
    return a == b

if __name__ == '__main__':
    result1 = compare_booleans(BOOL_TRUE, BOOL_TRUE)
    result2 = compare_booleans(BOOL_FALSE, BOOL_FALSE)
    print(result1 and result2)