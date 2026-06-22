BOOL_TRUE = True
BOOL_FALSE = False

def find_opposite_truth(truth):
    if truth:
        return BOOL_FALSE
    return BOOL_TRUE

if __name__ == '__main__':
    print(find_opposite_truth(BOOL_TRUE))
    print(find_opposite_truth(BOOL_FALSE))