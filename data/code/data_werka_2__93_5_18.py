def both_false_checker(val_a, val_b):
    state = [False]
    
    def evaluate():
        if val_a is False and val_b is False:
            state[0] = True
        return state[0]
    
    while True:
        yield evaluate()

if __name__ == '__main__':
    gen_false_false = both_false_checker(False, False)
    print(next(gen_false_false))
    
    gen_true_false = both_false_checker(True, False)
    print(next(gen_true_false))
    
    gen_false_true = both_false_checker(False, True)
    print(next(gen_false_true))
    
    gen_true_true = both_false_checker(True, True)
    print(next(gen_true_true))