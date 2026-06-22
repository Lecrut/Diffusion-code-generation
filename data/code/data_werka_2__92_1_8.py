TRUE = True
FALSE = False

def find_opposite_truth(value: bool) -> bool:
    if value:
        return FALSE
    return TRUE

if __name__ == '__main__':
    val_true = find_opposite_truth(TRUE)
    val_false = find_opposite_truth(FALSE)
    print(val_true)
    print(val_false)