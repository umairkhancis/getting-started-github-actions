import subprocess

print("This is python script")
subprocess.Popen('echo ::set-output name=MY_KEY::MY_VALUE', shell=True)
