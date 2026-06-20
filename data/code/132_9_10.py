def determine_outcome():
    x = True
    y = False
    z = True
    
    result = (x & y) | (~z)
    
    return result

if __name__ == '__main__':
    print(determine_outcome())