# Importing the 're' module for regular expressions, enabling pattern matching and extraction in log parsing.
import os
import re
import sys

def parse_log(log_file):
    # Regular expression pattern to match log entries with specific format
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+): (.*)')

    # Lists to store parsed data
    timestamps = []
    usernames = []
    messages = []

    # Read and parse each line in the log file
    with open(log_file, 'r', encoding='utf-8') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                # Extracting timestamp, username, and message from the log entry
                timestamp, username, message = match.groups()
                timestamps.append(timestamp)
                usernames.append(username)
                messages.append(message)

    # Print a simple report
    print("Timestamp\t       Username\t          Message")
    print("-----------------------------------------------------------")
    for i in range(len(timestamps)):
        print(f"{timestamps[i]}\t{usernames[i]:<15}\t{messages[i]}")

# Usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        log_file_path = sys.argv[1]
    elif os.path.exists("sample_auth.log"):
        log_file_path = "sample_auth.log"
    else:
        user_input = input("Enter log file path (or press Enter for 'sample_auth.log'): ").strip()
        log_file_path = user_input if user_input else "sample_auth.log"

    if os.path.exists(log_file_path):
        parse_log(log_file_path)
    else:
        print(f"Error: Log file '{log_file_path}' not found.")
