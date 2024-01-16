from argparse import FileType
from msilib.schema import SelfReg
import os
import pickle
from tabnanny import filename_only
from typing import Self
import PySimpleGUI as sg 

class Gui:
    def __init__(self):
        self.layout = [[sg.Text('Search Term: '), sg.Input()]]
        self.window = sg.Window('file Search Engine').layout(self.layout)
class SearchEngine:
    def __init__(self):
        self.file_index = [] #To store our directory index
        self.results = []
        self.matches = 0
        self.records = 0

        def create_new_index(self, root_path):
            '''create a new index and save to file'''
            self.file-index == [(root, files) for root, dirs, files in os.walk(root_path) if files]


            with open9(file: _OpenFile, mode: OpenTextMode = buffering : int = ..., encoding: str | None = ..., errors: str | None = ..., newline : str | None'file_index.pkl','wb':,
                pickle.dump(self.file_index, file )
                   def load_existing_index(self):
                        '''load existing index'''
            
            try:
                with open('file_index.pkl','rb') as f:
                    self.file_index = pickle.load(f)
            except self.file_index : []

        def search(self, term, search_type = 'contains'):
            '''search for term based on search type'''
            
            
         
         # reset variables
self.results.clear()         
         
Self.matches = 0
SelfReg.records = 0

         # to perform search
for path, files in self.file_index:
            for file in files:
                self.records += 1
                if(search_type == 'contains' and term.lower() in file.lower() or 
                search_type == 'startswith' and file.lower().startswith(term.lower()) or
                search_type == 'endswith' and file.lower().endswith(term.lower())):
                   result = path.replace('\\','/') + '/' + file
                self.results.append(result)
                self.matches += 1
            else:
                continue
        # save search results
with open('search_results.txt','w') as f:
            for row in self.results:
                f.write(row + '\n')

def test1():
    s = SearchEngine()
    s.create_new_index('c:/')
    s.search('gecko')

    print()
    print('>> There were {:,d} mathes out of {:,d} records searched.'.format(s.matches, s.records))
    print()
    print('>> This query produced the following matches: \n')
    for match in results:
        print(match)


def test2():
    g = Gui()
    g.window.Read():
