L = [4, 6, 8]
def get_box_surface():
    return sum(2 * a * b for a, b in [(L[i], L[i+1]) for i in range(3)])
if __name__ == '__main__':
    print(get_box_surface())