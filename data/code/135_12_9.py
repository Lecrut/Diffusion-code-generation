def are_equivalent(expr1, expr2):
    return expr1 == expr2

if __name__ == '__main__':
    e1 = True
    e2 = True
    print(f"Are {e1} and {e2} equivalent? {are_equivalent(e1, e2)}")
    
    e3 = True
    e4 = False
    print(f"Are {e3} and {e4} equivalent? {are_equivalent(e3, e4)}")
    
    e5 = False
    e6 = False
    print(f"Are {e5} and {e6} equivalent? {are_equivalent(e5, e6)}")