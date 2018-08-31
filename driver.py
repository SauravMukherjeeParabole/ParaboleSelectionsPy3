import logging
import os

#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def create_knowledge_graph(contents_of_input_file, name_of_input_file):
    # Through this function you have to use the contents of each file to create a knowledge graph
    # The output has to be saved in the data/output folder with the same name as data/input file
    # Note the writing to file has to be handled by you.
    pass

#Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Folder where the input files are present
    mypath = "data//input"
    list_of_input_files = read_directory(mypath)
    logging.debug(list_of_input_files)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()

            create_knowledge_graph(file_contents, each_file)
            # end of code