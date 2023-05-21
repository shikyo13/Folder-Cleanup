import os
import shutil
from pathlib import Path

def get_size(path):
    total = 0
    for path, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            total += os.path.getsize(fp)
    return total

def clean_folder(path, approved_exts):
    total_size = 0
    files_to_remove = []
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if not any(file.endswith(ext) for ext in approved_exts):
                file_path = os.path.join(root, file)
                files_to_remove.append(file_path)
                total_size += os.path.getsize(file_path)

    return files_to_remove, total_size

def remove_files(files_to_remove):
    for file in files_to_remove:
        os.remove(file)

def main():
    approved_exts = ['.jpg', '.doc', '.docx', '.xlsx', '.xls', '.pdf', '.jpeg', '.png']

    path = input("Enter the path to the folder you want to clean: ")

    # Check if path exists
    if not os.path.isdir(path):
        print(f"The path {path} does not exist.")
        return

    files_to_remove, total_size = clean_folder(path, approved_exts)
    
    if len(files_to_remove) == 0:
        print("No files to remove.")
        return
    
    print("The following files will be removed:")
    for file in files_to_remove:
        print(file)
    print(f"Total space to be saved: {total_size / (1024 * 1024):.2f} MB")
    
    confirm = input("Do you want to proceed? (yes/no): ")

    if confirm.lower() == 'yes':
        remove_files(files_to_remove)
        print("Cleanup complete.")
    else:
        print("Cleanup cancelled.")
        
if __name__ == "__main__":
    main()
