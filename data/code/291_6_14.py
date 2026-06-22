def compare_measures(nm, um):
    nm_to_um = 0.001
    if nm * nm_to_um < um:
        return f"{nm} nm"
    else:
        return f"{um} um"

if __name__ == '__main__':
    print(compare_measures(500, 0.3))