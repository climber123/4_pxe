import os, re
def get_names():
	i = 0
	j = 0
	start_path = r"C:\Users\ils\Desktop\netdrv\test1"
	destintaion_path = r"C:\1"
	win_version= ("7x64", "NTx64", "AllNT", "67x64", "78x64", "781x64", "7819x64")
	start_path = os.path.abspath (start_path)
	destintaion_path = os.path.abspath(destintaion_path)
	filenames_coteage = os.walk(start_path)
	y = ""
	i=0
	for root, dirs, files in os.walk(start_path):
		for name in dirs:
			current_path=os.path.join(root, name)
			if name in win_version:
				print(current_path) 
				os.system("mkdir " + destintaion_path + "\\" + str(i)) 
				os.system("xcopy /S " + current_path + " " + destintaion_path + "\\" + str(i))
				i = i + 1
get_names()