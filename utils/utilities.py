import arrow
import os
from pathlib import Path


def remove_old_files(path_to_directory, days=-7):
    # keep files for 7 days to make sure that this works also in a hpc environment
    print("Removing old temporary bash scripts.")
    
    criticalTime = arrow.now().shift().shift(days=days)

    for file in Path(path_to_directory).glob('*'):
        if file.is_file():
            file_time_modified = arrow.get(file.stat().st_mtime)
            if file_time_modified < criticalTime:
                os.remove(file)