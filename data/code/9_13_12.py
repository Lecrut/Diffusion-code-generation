from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from typing import Union

class VolumeUnit(Enum):
    L = "L"
    mL = "mL"
    m3 = "m3"
    gal = "gal"

def convert_volume(value: Union[int, float, Decimal], from_unit: VolumeUnit, to_unit: VolumeUnit) -> Decimal:
    if not isinstance(value, (int, float, Decimal)):
        raise TypeError("Value must be int, float, or Decimal")
    
    if from_unit == to_unit:
        return Decimal(str(value))
    
    factor_to_mL = {
        VolumeUnit.L: Decimal("1000"),
        VolumeUnit.mL: Decimal("1"),
        VolumeUnit.m3: Decimal("1000000"),
        VolumeUnit.gal: Decimal("3785.411784"),
    }
    
    factor_to_target = {
        VolumeUnit.L: Decimal("0.001"),
        VolumeUnit.mL: Decimal("1"),
        VolumeUnit.m3: Decimal("0.000001"),
        VolumeUnit.gal: Decimal("0.000264172"),
    }
    
    mL_value = Decimal(str(value)) * factor_to_mL[from_unit]
    
    result = mL_value * factor_to_target[to_unit]
    
    return result.quantize(Decimal("0.000000000000000000"), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    result = convert_volume(1, VolumeUnit.gal, VolumeUnit.L)
    print(result)