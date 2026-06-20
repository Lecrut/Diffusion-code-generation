if __name__ == '__main__':
    A = True
    B = True
    print(f"A: {A}, B: {B}, A implies B: {not A or B}")
    
    A = True
    B = False
    print(f"A: {A}, B: {B}, A implies B: {not A or B}")
    
    A = False
    B = True
    print(f"A: {A}, B: {B}, A implies B: {not A or B}")
    
    A = False
    B = False
    print(f"A: {A}, B: {B}, A implies B: {not A or B}")