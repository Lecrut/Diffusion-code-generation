import math
def simplify_ratios(ratios):
    simplified = {}
    for name, ratio in ratios.items():
        if ratio == 0:
            simplified[name] = "0"
        else:
            common = math.gcd(ratio)
            simplified[name] = ratio / common
    return simplified
if __name__ == '__main__':
    input_ratios = {
        "1:2": 4,
        "3:6": 18,
        "5:10": 25,
        "7:14": 35,
        "2:4": 100
    }
    result = simplify_ratios(input_ratios)
    print(result)