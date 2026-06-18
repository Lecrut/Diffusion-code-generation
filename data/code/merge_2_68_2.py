from dataclasses import dataclass
@dataclass(frozen=True)
class Gallon:
    value: float
@dataclass(frozen=True)
class Quart:
    value: float
@dataclass(frozen=True)
class Pint:
    value: float
@dataclass(frozen=True)
class Cup:
    value: float
@dataclass(frozen=True)
class FluidOunce:
    value: float
@dataclass(frozen=True)
class Liter:
    value: float
@dataclass(frozen=True)
class Milliliter:
    value: float
def gallon_to_quart(gallon: Gallon) -> Quart:
    return Quart(value=gallon.value * 4.0)
def quart_to_pint(quart: Quart) -> Pint:
    return Pint(value=quart.value / 2.0)
def pint_to_cup(pint: Pint) -> Cup:
    return Cup(value=pint.value * 2.0)
def cup_to_fluid_ounce(cup: Cup) -> FluidOunce:
    return FluidOunce(value=cup.value * 8.0)
def fluid_ounce_to_milliliter(fluid_ounce: FluidOunce) -> Milliliter:
    return Milliliter(value=fluid_ounce.value * 29.5735296)
def milliliter_to_liter(milliliter: Milliliter) -> Liter:
    return Liter(value=milliliter.value / 1000.0)
def liter_to_gallon(liter: Liter) -> Gallon:
    return Gallon(value=liter.value * 378541.17962864)
if __name__ == '__main__':
    sample = Gallon(10.0)
    quart_result = gallon_to_quart(sample)
    pint_result = quart_to_pint(quart_result)
    cup_result = pint_to_cup(pint_result)
    ounce_result = cup_to_fluid_ounce(cup_result)
    ml_result = fluid_ounce_to_milliliter(ounce_result)
    liter_result = milliliter_to_liter(ml_result)
    final_gallon = liter_to_gallon(liter_result)
    print(f"Original Gallons: {final_gallon.value}")