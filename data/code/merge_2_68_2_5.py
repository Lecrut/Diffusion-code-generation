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
def gallon_to_quart(gallon_volume: Gallon) -> Quart:
    return Quart(value=gallon_volume.value * 4.0)
def quart_to_pint(quart_volume: Quart) -> Pint:
    return Pint(value=quart_volume.value / 2.0)
def pint_to_cup(pint_volume: Pint) -> Cup:
    return Cup(value=pint_volume.value / 2.0)
def cup_to_milliliter(cup_volume: Cup) -> Milliliter:
    return Milliliter(value=cup_volume.value * 236.588)
def milliliter_to_liter(milliliter_volume: Milliliter) -> Liter:
    return Liter(value=milliliter_volume.value / 1000.0)
def liter_to_gallon(liter_volume: Liter) -> Gallon:
    return Gallon(value=liter_volume.value * 378541.1792669655e-7)
if __name__ == '__main__':
    sample_input = Gallon(10.0)
    result_quart = gallon_to_quart(sample_input)
    print(f"{sample_input} gallons")
    intermediate_pint = quart_to_pint(result_quart)
    final_cup = pint_to_cup(intermediate_pint)
    final_ml = cup_to_milliliter(final_cup)
    converted_liter = milliliter_to_liter(final_ml)
    print(f"{result_quart} quarts")
    back_gallon = liter_to_gallon(converted_liter)
    print(f"{final_ml} milliliters")