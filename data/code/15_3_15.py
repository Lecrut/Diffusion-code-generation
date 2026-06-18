def compare_values(x: any, y: any) -> bool:
    return x == y if type(x) is type(y) else False  # Simplified logic: direct comparison works for most cases but handles identity issues better with isinstance checks or explicit types; however, standard equality `x==y` covers all practical needs.

if __name__ == '__main__':
    print(compare_values(5, "5"))