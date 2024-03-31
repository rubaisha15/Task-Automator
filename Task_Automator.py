import os
import psutil
import pandas as pd
import time

def organize_files():
    directories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "CSV": [".csv"],
    }

    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

    current_dir = os.getcwd()

    for filename in os.listdir(current_dir):
        if os.path.isfile(filename):
            for directory, extensions in directories.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    try:
                        if directory == 'Documents' and filename.lower().endswith('.csv'):
                            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, 'CSV', filename))
                            print(f"Moved {filename} to CSV directory.")
                        else:
                            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, directory, filename))
                            print(f"Moved {filename} to {directory} directory.")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")

def clean_data():
    filename = 'enterprise-counts-march-2023-csv-tables.csv'
    
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found! Please make sure the file exists.")
        return
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
        return

    try:
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
    except Exception as e:
        print(f"Error cleaning data: {e}")
        return
    
    cleaned_filename = 'cleaned_data.csv'
    try:
        df.to_csv(cleaned_filename, index=False)
        print(f"Data cleaning process executed. Cleaned data saved to {cleaned_filename}.")
    except Exception as e:
        print(f"Error saving cleaned data: {e}")

def maintain_system():
    print("Initiating System Maintenance...")
    time.sleep(1)
    
    print("\nWelcome to System Explorer!")
    print("You are now inside your system. Let's explore!")
    print("You find yourself in a virtual environment.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Check disk space")
        print("2. Explore running processes")
        print("3. Stop a running process")
        print("4. Exit System Explorer")

        choice = input("Enter the corresponding number: ")

        if choice == '1':
            try:
                disk_usage = psutil.disk_usage('/')
                print("\nAnalyzing disk space...")
                time.sleep(1)
                print(f"\nTotal disk space: {disk_usage.total / (1024*1024*1024):.2f} GB")
                print(f"Used disk space: {disk_usage.used / (1024*1024*1024):.2f} GB")
                print(f"Free disk space: {disk_usage.free / (1024*1024*1024):.2f} GB")
            except Exception as e:
                print(f"Error checking disk space: {e}")
        elif choice == '2':
            try:
                print("\nExploring running processes...")
                time.sleep(1)
                print("\nList of running processes:")
                for proc in psutil.process_iter(['pid', 'name']):
                    print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")
            except Exception as e:
                print(f"Error exploring running processes: {e}")
        elif choice == '3':
            process_id = input("\nEnter the PID of the process you want to stop: ")
            try:
                process_id = int(process_id)
                process = psutil.Process(process_id)
                process.terminate()
                print(f"\nProcess with PID {process_id} has been terminated.")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                print(f"\nError: {e}. Please enter a valid PID.")
            except Exception as e:
                print(f"\nError stopping process: {e}")
        elif choice == '4':
            print("\nExiting System Explorer...")
            break
        else:
            print("\nInvalid choice! Please select a valid option.")

    print("System Explorer has been shut down.")

def main():
    print("Welcome to Automation Script!")
    while True:
        print("\nWhat task would you like to perform?")
        print("1. Organize files")
        print("2. Clean data")
        print("3. Maintain system")
        print("4. Exit")

        choice = input("Enter the corresponding number: ")

        if choice == '1':
            organize_files()
        elif choice == '2':
            clean_data()
        elif choice == '3':
            maintain_system()
        elif choice == '4':
            print("Shutting down.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

        another_task = input("Do you want to perform another task? (yes/no): ")
        if another_task.lower() != 'yes':
            print("Shutting down.")
            break

if __name__ == "__main__":
    main()
