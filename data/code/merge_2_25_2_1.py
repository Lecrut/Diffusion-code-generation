import asyncio
from typing import Dict, List, Tuple
import aiohttp
class CoordinateCache:
    def __init__(self):
        self._cache: Dict[Tuple[int, int], str] = {}
        self.lock = asyncio.Lock()
    async def get(self, coord: Tuple[int, int]) -> str:
        if coord in self._cache:
            return self._cache[coord]
        await asyncio.sleep(0.1)
        new_name = f"Location_{coord[0]}_{coord[1]}"
        async with self.lock:
            if coord in self._cache:
                return self._cache[coord]
            if coord not in self._cache:
                self._cache[coord] = new_name
            return new_name
    async def set(self, coord: Tuple[int, int], name: str):
        async with self.lock:
            self._cache[coord] = name
async def fetch_coordinates(session: aiohttp.ClientSession) -> List[Tuple[str, str]]:
    coords_data = [
        (101, 205),
        (304, 789),
        (666, 123),
        (999, 888),
        (42, 42)
    ]
    tasks = [session.get(f"http://example.com/api?x={c[0]}&y={c[1]}") for c in coords_data]
    results = await asyncio.gather(*tasks)
    return [(str(c), r.text.strip()) if not isinstance(r, str) else (str(c), r) for c, r in zip(coords_data, results)]
async def main():
    cache = CoordinateCache()
    coordinator_map: Dict[Tuple[int, int], str] = {}
    sample_coords = [(101, 205), (304, 789), (666, 123)]
    for coord in sample_coords:
        name = await cache.get(coord)
        coordinator_map[coord] = name
    test_coord = (101, 205)
    cached_name = await cache.get(test_coord)
    print(f"Initial mapping for {test_coord}: {cached_name}")
if __name__ == '__main__':
    asyncio.run(main())