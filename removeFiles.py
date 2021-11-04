import os
import shutil
import time
def remove():
	ts(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= get_file_or_folder_age(root_folder):
				remove_folder(root_folder)
				ReRemovedFolders = 0
	RemovedFiles = 0
    path = "/PATH_TO_DELETE"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)
    if os.path.exismovedFolders += 1
				break
			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= get_file_or_folder_age(folder_path):
						remove_folder(folder_path)
						RemovedFolders += 1 
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= get_file_or_folder_age(file_path):
						remove_file(file_path)
						RemovedFiles += 1 

		else:
			if seconds >= get_file_or_folder_age(path):	
				remove_file(path)
				RemovedFiles += 1 

	else:
		print(f'"{path}" is not found')
		RemovedFiles += 1 

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):
    if not shutil.rmtree(path):
		print(f"{path} is removed successfully")
	else:
		print(f"Unable to delete the "+path)
def remove_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")
	else:
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	ctime = os.stat(path).st_ctime
	return ctime


if __name__ == '__remove__':
	remove()