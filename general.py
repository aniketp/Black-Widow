import os


# Each website that you crawl is a separate file
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Created directory " + directory)
        os.makedirs(directory)


# Create queue and crawled files (If not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        make_file(queue, base_url)

    if not os.path.isfile(crawled):
        make_file(crawled, " ")


# Create a new file
def make_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# Add data to an existing file
def add_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + "\n")
        file.close()


# Delete contents form a file
def delete_fron_file(path):
    with open(path, "w"):
        pass


# Read a file and convert each line to set item
def file_to_set(path_name):
    urls = set()
    with open(path_name, "rt") as file:
        for line in file:
            urls.add(line.replace('\n', ''))
    return urls


# Write set items to a file as distinct lines
def set_to_file(links, file):
    delete_fron_file(file)
    for link in sorted(links):
        add_to_file(file, link)