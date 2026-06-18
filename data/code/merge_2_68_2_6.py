import dataclasses
from typing import Union
@dataclasses.dataclass(frozen=True)
class Gallon:
    value: float
@dataclasses.dataclass(frozen=True)
class Quart:
    value: float
@dataclasses.dataclass(frozen=True)
class Pint:
    value: float
@dataclasses.dataclass(frozen=True)
class Cup:
    value: float
@dataclasses.dataclass(frozen=True)
class Liter:
    value: float
@dataclasses.dataclass(frozen=True)
class Milliliter:
    value: float
def gallon_to_quart(gallon_value: Union[int, float]) -> Quart:
    return Quart(value=gallon_value * 4.0)
def quart_to_pint(quart_value: Union[int, float]) -> Pint:
    return Pint(value=quart_value / 2.0)
def pint_to_cup(pint_value: Union[int, float]) -> Cup:
    return Cup(value=pint_value * 2.0)
def cup_to_milliliter(cup_value: Union[int, float]) -> Milliliter:
    return Milliliter(value=cup_value * 236.588)
def milliliter_to_liter(milliliter_value: Union[int, float]) -> Liter:
    return Liter(value=milliliter_value / 1000.0)
if __name__ == '__main__':
    sample_gallon = Gallon(2)
    quart_result = gallon_to_quart(sample_gallon.value)
    pint_result = quart_to_pint(quart_result.value)
    cup_result = pint_to_cup(pint_result.value)
    ml_result = cup_to_milliliter(cup_result.value)
    liter_result = milliliter_to_liter(ml_result.value)
    print(f"{sample_gallon} gallons")
    print(f"= {quart_result} quarts")
    print(f"= {pint_result} pints")
    print(f"= {cup_result} cups")
    print(f"= {ml_result} milliliters")
    print(f"= {liter_result} liters")