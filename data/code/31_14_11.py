def get_area(side):
    return side * side

def run_calculation():
    config = {"side": 50}
    return get_area(config["side"])

if __name__ == "__main__":
    print(run_calculation())