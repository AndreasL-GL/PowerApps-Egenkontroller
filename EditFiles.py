import sys
import os
import json

solution_path = sys.argv[-1]

def change_list_Id(solution_path,ListFinishedReportID, ListReportID, ListControlID, ListNavigationID, ListVariablesID, ProjectName, SharepointSiteUrl):
    for root, _ , files in os.walk(solution_path):
        for file in files:
            fpath = os.path.join(root,file)
            
            if "environmentvariabledefinitions" in root:
                if "al_List_finished_report" in root and ".json" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    old_finishedReportID = js["environmentvariablevalues"]["environmentvariablevalue"]["value"]
                    js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = ListFinishedReportID
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,ensure_ascii=False,indent=2)
                        
                elif "al_shared_sharepointonline_29bcca241e624455b4318404ae715111" in root and ".json" in file:
                    print("HELLO")
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    old_reportID = js["environmentvariablevalues"]["environmentvariablevalue"]["value"]
                    js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = ListReportID
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,ensure_ascii=False,indent=2)
                                
                elif "al_shared_sharepointonline_6a1ce7de7b664e3aa6ef01086adac5d6" in root and ".json" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    old_ControlID = js["environmentvariablevalues"]["environmentvariablevalue"]["value"]
                    js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = ListControlID
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,ensure_ascii=False,indent=2)
                        
                elif "al_List_Navigation" in root and ".json" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    old_NavigationID = js["environmentvariablevalues"]["environmentvariablevalue"]["value"]
                    js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = ListNavigationID
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,ensure_ascii=False,indent=2)
                        
                elif "al_List_Variables" in root and ".json" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    old_VariableID = js["environmentvariablevalues"]["environmentvariablevalue"]["value"]
                    js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = ListVariablesID
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,ensure_ascii=False,indent=2)
                
                elif "al_Project_name" in root and ".json" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    old_Project_name = js["environmentvariablevalues"]["environmentvariablevalue"]["value"]
                    js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = ProjectName
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,ensure_ascii=False,indent=2)
                        
                elif "al_SharepointSiteURL" in root and ".json" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    old_SharepointSiteURL = js["environmentvariablevalues"]["environmentvariablevalue"]["value"]
                    js["environmentvariablevalues"]["environmentvariablevalue"]["value"] = SharepointSiteUrl
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,ensure_ascii=False,indent=2)
                        
                elif "al_Sharepoint_Site" in root and ".xml" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        xml = f.read()
                        xml = xml.split('<defaultvalue>')[0]+'<defaultvalue>' + SharepointSiteUrl +'</defaultvalue>'+ xml.split('</defaultvalue>')[1]
                    xml = xml.replace("https://greenlandscapingmalmo.sharepoint.com/sites/Avvikelsehantering2",SharepointSiteUrl)
                    with open(fpath,'w',encoding='utf-8') as f:
                        f.write(xml)
                
            if "CanvasApps" in root:
                if "Connections.json" in file:
                    with open(fpath,'r',encoding='utf-8') as f:
                        js = json.load(f)
                    for key,value in js.items():
                        
                        if "List_control" in json.dumps(value['datasets']):
                            datasets = {
      SharepointSiteUrl+"_al_SharepointSiteURL": {
        "datasetOverride": {
          "environmentVariableName": "al_SharepointSiteURL"
        },
        "dataSources": {
          "List_Control": {
            "tableName": ListControlID,
            "tableNameOverride": {
              "environmentVariableName": "al_shared_sharepointonline_6a1ce7de7b664e3aa6ef01086adac5d6"
            }
          },
          "List_Report": {
            "tableName": ListReportID,
            "tableNameOverride": {
              "environmentVariableName": "al_shared_sharepointonline_29bcca241e624455b4318404ae715111"
            }
          }
        }
      }
    }
                            value['datasets'] = datasets
                        elif "al_List_finished_report" in json.dumps(value['datasets']):
                            datasets = {
      SharepointSiteUrl+"_al_SharepointSiteURL": {
        "datasetOverride": {
          "environmentVariableName": "al_SharepointSiteURL"
        },
        "dataSources": {
          "List_finished_report": {
            "tableName": ListFinishedReportID,
            "tableNameOverride": {
              "environmentVariableName": "al_List_finished_report"
            }
          },
          "List_Navigation": {
            "tableName": ListNavigationID,
            "tableNameOverride": {
              "environmentVariableName": "al_List_Navigation"
            }
          },
          "List_Variables": {
            "tableName": ListVariablesID,
            "tableNameOverride": {
              "environmentVariableName": "al_List_Variables"
            }
          }
        }
      }
    }
                            value['datasets'] = datasets
                        
                    with open(fpath,'w',encoding='utf-8') as f:
                        json.dump(js,f,indent=2,ensure_ascii=False)
    old_Ids = [old_reportID,old_finishedReportID,old_ControlID,old_NavigationID,old_VariableID]
    new_Ids = [ListReportID, ListFinishedReportID, ListControlID, ListNavigationID, ListVariablesID]
    filenames = ["List_report.json", "List_finished_report.json", "List_Control.json", "List_Navigation.json", "List_Variables.json"]
    if True:
        for root, _ , files in os.walk(solution_path):
            for file in files:
                fpath = os.path.join(root,file)
                for old,new,fname in zip(old_Ids,new_Ids, filenames):
                    if fname in fpath and "TableDefinitions" in fpath:
                        try:
                            with open(fpath,'r',encoding='utf-8') as f:
                                x = f.read()
                            with open(fpath,'w', encoding='utf-8') as f:
                                f.write(x.replace(old,new))
                        except:pass
                try:
                    with open(fpath,'r',encoding='utf-8') as f:
                        text = f.read()
                    if "Report_app" in text:
                        print(fpath)
                        with open(fpath,'w',encoding='utf-8') as f:
                            f.write(text.replace('Report_app',ProjectName))
                            
                except: pass
                if "Solution.xml" in fpath:
                    with open(fpath,'r',encoding='utf-8') as f:
                        x = f.read()
                    with open(fpath,'w', encoding='utf-8') as f:
                        f.write(x.replace("Egenkontroller",ProjectName+"App"))
                
                        
                    #with open(fpath, 'w', encoding='utf-8') as f:
                        #f.write(x)
                        
        
                        
                        
# change_list_Id(solution_path, "ff034583-73d4-4220-90f4-dafc5cf246f7","25699c65-d136-4833-bf46-49fd003f838b","60907c6b-3d07-43db-bbd8-26243c989e00","8a126430-200c-48d2-814c-0e63a8c029ac","e8cc5f80-bf3c-4ea6-9fa8-92755e796143","MyTestProject","https://greenlandscapingmalmo.sharepoint.com/sites/Avvikelsehantering2")


finishedListreportid="ff034583-73d4-4220-90f4-dafc5cf246f7"
ReportId = "25699c65-d136-4833-bf46-49fd003f838b"
ControlId = "60907c6b-3d07-43db-bbd8-26243c989e00"
NavigationId = "8a126430-200c-48d2-814c-0e63a8c029ac"
VariablesID = "e8cc5f80-bf3c-4ea6-9fa8-92755e796143"
ProjectName = "MyTestProject"
SharepointSiteUrl = "https://greenlandscapingmalmo.sharepoint.com/sites/Avvikelsehantering2"
if len(sys.argv) == 9:
    (filename, solution_path,finishedListreportid, ReportId, ControlId, NavigationId, VariablesID, ProjectName, SharepointSiteUrl) = sys.argv
    print("filename: ", filename)
    print("solution_path: ", "solution_path")
    print("ProjectName: ", ProjectName)
    print("SharepointSiteUrl", SharepointSiteUrl) 
    if True:
        change_list_Id(solution_path, finishedListreportid, ReportId, ControlId, NavigationId, VariablesID, ProjectName, SharepointSiteUrl)
        # with open(r"C:\Users\anlo22\OneDrive - GLnet\Dokument\Code\Projects\2023-10-19 AzureDevops Egenkontroller\CanvasApps\App\pkgs\TableDefinitions\List_Report.json", 'r',encoding='utf-8') as f:
        #     js = json.load(f)
        # with open(r"C:\Users\anlo22\OneDrive - GLnet\Dokument\Code\Projects\2023-10-19 AzureDevops Egenkontroller\CanvasApps\App\pkgs\TableDefinitions\List_Report2.json", 'w',encoding='utf-8') as f:
        #     js['TableName'] = ReportId
        #     item = json.loads(js['DataEntityMetadataJson'][list(js['DataEntityMetadataJson'].keys())[0]])
        #     print(json.dumps(item,indent=2,ensure_ascii=False))
else:
    print("All arguments not present.")
    print(len(sys.argv))
    print(sys.argv)
