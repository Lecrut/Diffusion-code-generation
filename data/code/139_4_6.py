gates = {
    'and': lambda a, b: a & b,
    'or': lambda a, b: a | b,
    'not': lambda a: ~a,
    'xor': lambda a, b: a ^ b
}

if __name__ == '__main__':
    result_and = gates['and'](10, 5)
    print(f"AND of 10 and 5 is: {result_and}")
    
    result_or = gates['or'](10, 5)
    print(f"OR of 10 and 5 is: {result_or}")
    
    result_not = gates['not'](-3)
    print(f"NOT of -3 is: {result_not}")
    
    result_xor = gates['xor'](10, 5)
    print(f"XOR of 10 and 5 is: {result_xor}")