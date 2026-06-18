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
def gallon_to_quart(gallons: Gallon) -> Quart:
    return Quart(value=gallons.value * 4.0)
def quart_to_pint(quarts: Quart) -> Pint:
    return Pint(value=quarts.value / 2.0)
def pint_to_cup(pints: Pint) -> Cup:
    return Cup(value=pints.value * 2.0)
def cup_to_liter(cups: Cup) -> Liter:
    return Liter(value=cups.value * 0.00147868)
def liter_to_gallon(liters: Liter) -> Gallon:
    return Gallon(value=liters.value / 3.785412)
if __name__ == '__main__':
    sample = Gallon(1.0)
    print(f"{sample} gallons")
    q = gallon_to_quart(sample)
    print(f"-> {q} quarts")
    p = quart_to_pint(q)
    print(f"-> {p} pints")
    c = pint_to_cup(p)
    print(f"-> {c} cups")
    l = cup_to_liter(c)
    print(f"-> {l} liters")
    g_back = liter_to_gallon(l)
    print(f"<- {g_back} gallons (round trip check)")