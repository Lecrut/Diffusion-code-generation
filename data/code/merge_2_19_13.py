import pandas as pd
import numpy as np
import logging
from datetime import datetime
from pathlib import Path
import hashlib
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
    handlers=[
        logging.FileHandler('pipeline_debug.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
class DataPipeline:
    def __init__(self):
        self.cache_dir = Path("cache")
        self.cache_dir.mkdir(exist_ok=True)
        raw_data_dict = {
            'id': [1, 2, None, 4],
            'name': ['Alice', '', 'Bob', np.nan],
            'age': [30.5, -5, 25, float('inf')],
            'score': [85.67, 90.01, 78.44, None]
        }
        self.raw_df = pd.DataFrame(raw_data_dict)
    def validate_and_clean(self):
        logger.info("Starting validation phase...")
        if self.raw_df['id'].isnull().any():
            raise ValueError(f"Null value detected in required field 'id' at index {self.raw_df[self.raw_df['id'].isnull()].index.tolist()[0]}")
        invalid_age_mask = (self.raw_df['age'] < 0) | (~np.isfinite(self.raw_df['age']))
        if invalid_age_mask.any():
            raise ValueError(f"Invalid age value detected at index {[i for i, val in enumerate(invalid_age_mask.values()) if val]}")
        self.clean_df = self.raw_df.copy()
        logger.debug("Imputing null scores with column median...")
        score_median = self.clean_df['score'].median(skipna=True) if not self.clean_df['score'].isnull().all() else 0.0
        self.clean_df['name'] = self.clean_df['name'].fillna('Unknown')
    def process_intermediate(self):
        logger.info("Executing intermediate transformation...")
        max_age_expected = 120.0
        self.clean_df['normalized_age'] = (self.clean_df['age'].astype(float) / max_age_expected * 100).round(2)
        df_hash_key = hashlib.md5(self.clean_df.to_string().encode()).hexdigest()[:8]
        self.cache_filename = f"intermediate_step_{df_hash_key}.pkl"
        self.cache_file_path = self.cache_dir / self.cache_filename
        logger.debug(f"Checking for existing cache: {self.cache_file_name}")
        try:
            import pickle
            if not self.cache_file_exists():
                logger.warning("Cache miss. Generating new intermediate data...")
                result = np.array([x * 2 for x in self.clean_df['normalized_age'].values])
                cache_data = {
                    'df': self.clean_df,
                    'result_array': result,
                    'timestamp': datetime.now().isoformat()
                }
                with open(self.cache_file_path, 'wb') as f:
                    pickle.dump(cache_data, f)
            else:
                logger.info("Cache hit. Loading precomputed data...")
        except Exception as e:
            logger.error(f"Error during caching process: {e}")
    def cache_file_exists(self):
        return self.cache_file_path.exists() and self.cache_file_path.suffix == '.pkl'
def run_pipeline():
    pipeline = DataPipeline()
    try:
        pipeline.validate_and_clean()
        logger.info("Validation passed. Proceeding to transformation.")
        intermediate_result = pipeline.process_intermediate()
        if isinstance(intermediate_result, np.ndarray):
            logger.debug(f"Intermediate result shape: {intermediate_result.shape}")
    except Exception as e:
        logger.critical(f"Pipeline execution failed with error: {e}", exc_info=True)
if __name__ == '__main__':
    run_pipeline()