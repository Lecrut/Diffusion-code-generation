FALSE = False
TRUE = True

def determine_both_false(val1, val2):
    is_false_1 = not bool(val1)
    is_false_2 = not bool(val2)
    return is_false_1 and is_false_2

if __name__ == '__main__':
    val1 = 0
    val2 = 0
    output = determine_both_false(val1, val2)
    print(output)
    
    val3 = 1
    val4 = 0
    output2 = determine_both_false(val3, val4)
    print(output2)
    
    val5 = None
    val6 = None
    output3 = determine_both_false(val5, val6)
    print(output3)
    
    val7 = []
    val8 = {}
    output4 = determine_both_false(val7, val8)
    print(output4)
    
    val9 = [1]
    val10 = {1: 1}
    output5 = determine_both_false(val9, val10)
    print(output5)