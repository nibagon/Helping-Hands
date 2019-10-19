import sys,os

print("Installing modules...")
os.system("pip3 install -r requirements.txt")
print("Modules installed!")
print("Running test...")
os.system("python3 module_test.py");
print("OK")
