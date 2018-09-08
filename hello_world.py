import json

class HelloWorld:
    def _output_types(self):
        return {
            'console': {'func': self._to_console},
            'file': {'func': self._to_file}
        }    
    
    def write(self):        
        ot = self._output_types()[self._output_type]
            
        ot['func']()
    
    def _to_console(self):
        print(self.msg)
        
    def _to_file(self):
        f_options = self._config['file_options']
        
        with open(f_options['file'], 'w') as file:
            file.write(self.msg)
        
    def __init__(self, msg='Hello World'):
        self.msg = msg
        
        with open('app.config') as cfg_file:            
            self._config = json.load(cfg_file)
            
            if 'output_type' in self._config and self._config['output_type'] in self._output_types():
                self._output_type = self._config['output_type']
            else:
                # default to console
                self._output_type = 'console'
                
