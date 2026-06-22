DIVISIBILITY_FLAGS = [
    ("century_check", lambda y: y % 100 == 0),
    ("quadrennium_check", lambda y: y % 4 == 0),
    ("quadcentury_check", lambda y: y % 400 == 0),
]

def is_leap_year(year):
    is_quadruple = DIVISIBILITY_FLAGS[1][1](year)
    is_century = DIVISIBILITY_FLAGS[0][1](year)
    is_quad_century = DIVISIBILITY_FLAGS[2][1](year)
    
    if is_quad_century:
        return True
    if is_century:
        return False
    if is_quadruple:
        return True
    return False

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(100))
    print(is_leap_year(200))