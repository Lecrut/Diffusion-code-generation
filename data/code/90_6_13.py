def check_conditions(*conditions):
    return any(condition() for condition in conditions)

if __name__ == '__main__':
    def condition1():
        return 5 > 0
    
    def condition2():
        return 3 == 3
    
    print(check_conditions(condition1, condition2))