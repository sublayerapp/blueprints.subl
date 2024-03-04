import sublime
import sublime_plugin
import requests

class SublayerBlueprintsSubmitBlueprintCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selected_text = self.view.substr(self.view.sel()[0])
        json_data = {"code": selected_text}
        url = "http://localhost:3000/api/v1/blueprints"  # Adjust server URL if needed

        try:
            response = requests.post(url, json=json_data)
            response.raise_for_status()  # Raise an exception for error status codes
            sublime.message_dialog("Blueprint submitted successfully.")
        except requests.exceptions.RequestException as e:
            sublime.error_message(sublime.error_message("Error submitting blueprint: {}".format(e)))

class SublayerBlueprintsReplaceSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selected_text = self.view.substr(self.view.sel()[0])
        json_data = {"description": selected_text}
        url = "http://localhost:3000/api/v1/blueprint_variants"  # Adjust server URL if needed

        try:
            response = requests.post(url, json=json_data)
            response.raise_for_status()
            self.view.replace(edit, self.view.sel()[0], response.data["result"])
        except requests.exceptions.RequestException as e:
            sublime.error_message(sublime.error_message("Error submitting blueprint: {}".format(e)))