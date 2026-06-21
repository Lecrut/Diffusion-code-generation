from typing import Union

def calculate_final_price(price: Union[int, float], discount_rate: float) -> Union[int, float]:
    return price * (1 - discount_rate)

if __name__ == '__main__':
    input_price = 200
    discount = 0.40
    result = calculate_final_price(input_price, discount)
    print(result)