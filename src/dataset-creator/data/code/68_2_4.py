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
def gallon_to_quarts(gallons: Gallon) -> Quart:
    return Quart(value=gallons.value * 4.0)
def quart_to_pints(quart: Quart) -> Pint:
    return Pint(value=quart.value * 2.0)
def pint_to_cups(pint: Pint) -> Cup:
    return Cup(value=pint.value * 2.0)
def cup_to_liters(cup: Cup) -> Liter:
    return Liter(value=cup.value / 48.95741366696)
def liter_to_gallons(liter: Liter) -> Gallon:
    return Gallon(value=liter.value * 0.264172052)
if __name__ == '__main__':
    sample = Gallon(8.0)
    result_qt = gallon_to_quarts(sample)
    print(f"{result_qt}")
    intermediate_pint = quart_to_pints(result_qt)
    final_cup = pint_to_cups(intermediate_pint)
    print(f"{final_cup}")
    metric_liters = cup_to_liters(final_cup)
    print(f"{metric_liters}")
    back_gallons = liter_to_gallons(metric_liters)
    print(f"{back_gallons}")