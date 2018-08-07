# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gps_importer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatchGpsImporter(object):
    def setupUi(self, BatchGpsImporter):
        BatchGpsImporter.setObjectName("BatchGpsImporter")
        BatchGpsImporter.setEnabled(True)
        BatchGpsImporter.resize(587, 437)
        self.horizontalLayout = QtWidgets.QHBoxLayout(BatchGpsImporter)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(BatchGpsImporter)
        self.tab_widget.setMinimumSize(QtCore.QSize(556, 0))
        self.tab_widget.setObjectName("tab_widget")
        self.input_output_tab = QtWidgets.QWidget()
        self.input_output_tab.setObjectName("input_output_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.input_output_tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(29)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.input_output_tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.input_gpx_folder = QtWidgets.QLineEdit(self.input_output_tab)
        self.input_gpx_folder.setObjectName("input_gpx_folder")
        self.gridLayout.addWidget(self.input_gpx_folder, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.input_output_tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.route = QtWidgets.QCheckBox(self.input_output_tab)
        self.route.setChecked(True)
        self.route.setObjectName("route")
        self.gridLayout.addWidget(self.route, 3, 3, 1, 1)
        self.input_gpx_file_btn = QtWidgets.QPushButton(self.input_output_tab)
        self.input_gpx_file_btn.setObjectName("input_gpx_file_btn")
        self.gridLayout.addWidget(self.input_gpx_file_btn, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.input_output_tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.geometry_type_cbo = QtWidgets.QComboBox(self.input_output_tab)
        self.geometry_type_cbo.setObjectName("geometry_type_cbo")
        self.gridLayout.addWidget(self.geometry_type_cbo, 5, 1, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.input_output_tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.no_scan_sub_folders_rbtn = QtWidgets.QRadioButton(self.input_output_tab)
        self.no_scan_sub_folders_rbtn.setObjectName("no_scan_sub_folders_rbtn")
        self.gridLayout.addWidget(self.no_scan_sub_folders_rbtn, 2, 2, 1, 1)
        self.scan_sub_folders_rdb = QtWidgets.QRadioButton(self.input_output_tab)
        self.scan_sub_folders_rdb.setChecked(True)
        self.scan_sub_folders_rdb.setObjectName("scan_sub_folders_rdb")
        self.gridLayout.addWidget(self.scan_sub_folders_rdb, 2, 1, 1, 1)
        self.input_projection_cbo = QgsProjectionSelectionWidget(self.input_output_tab)
        self.input_projection_cbo.setMaximumSize(QtCore.QSize(16777215, 23))
        self.input_projection_cbo.setObjectName("input_projection_cbo")
        self.gridLayout.addWidget(self.input_projection_cbo, 6, 1, 1, 3)
        self.track = QtWidgets.QCheckBox(self.input_output_tab)
        self.track.setChecked(True)
        self.track.setObjectName("track")
        self.gridLayout.addWidget(self.track, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.input_output_tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.waypoint = QtWidgets.QCheckBox(self.input_output_tab)
        self.waypoint.setChecked(True)
        self.waypoint.setObjectName("waypoint")
        self.gridLayout.addWidget(self.waypoint, 3, 2, 1, 1)
        self.layer_name_edit = QtWidgets.QLineEdit(self.input_output_tab)
        self.layer_name_edit.setMaxLength(50)
        self.layer_name_edit.setObjectName("layer_name_edit")
        self.gridLayout.addWidget(self.layer_name_edit, 4, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.input_output_tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.prefix_label = QtWidgets.QLabel(self.input_output_tab)
        self.prefix_label.setObjectName("prefix_label")
        self.gridLayout.addWidget(self.prefix_label, 1, 0, 1, 1)
        self.suffix_label = QtWidgets.QLabel(self.input_output_tab)
        self.suffix_label.setObjectName("suffix_label")
        self.gridLayout.addWidget(self.suffix_label, 1, 2, 1, 1)
        self.file_name_prefix = QtWidgets.QLineEdit(self.input_output_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name_prefix.sizePolicy().hasHeightForWidth())
        self.file_name_prefix.setSizePolicy(sizePolicy)
        self.file_name_prefix.setObjectName("file_name_prefix")
        self.gridLayout.addWidget(self.file_name_prefix, 1, 1, 1, 1)
        self.file_name_suffix = QtWidgets.QLineEdit(self.input_output_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name_suffix.sizePolicy().hasHeightForWidth())
        self.file_name_suffix.setSizePolicy(sizePolicy)
        self.file_name_suffix.setObjectName("file_name_suffix")
        self.gridLayout.addWidget(self.file_name_suffix, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tab_widget.addTab(self.input_output_tab, "")
        self.validation_tab = QtWidgets.QWidget()
        self.validation_tab.setObjectName("validation_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.validation_tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.invalid_gpx_folder = QtWidgets.QLineEdit(self.validation_tab)
        self.invalid_gpx_folder.setObjectName("invalid_gpx_folder")
        self.gridLayout_2.addWidget(self.invalid_gpx_folder, 6, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.validation_tab)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.invalid_folder_btn = QtWidgets.QPushButton(self.validation_tab)
        self.invalid_folder_btn.setObjectName("invalid_folder_btn")
        self.gridLayout_2.addWidget(self.invalid_folder_btn, 6, 3, 1, 1)
        self.valid_folder_btn = QtWidgets.QPushButton(self.validation_tab)
        self.valid_folder_btn.setObjectName("valid_folder_btn")
        self.gridLayout_2.addWidget(self.valid_folder_btn, 5, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.validation_tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)
        self.exclude_with_few_points = QtWidgets.QRadioButton(self.validation_tab)
        self.exclude_with_few_points.setObjectName("exclude_with_few_points")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(BatchGpsImporter)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.exclude_with_few_points)
        self.gridLayout_2.addWidget(self.exclude_with_few_points, 4, 1, 1, 1)
        self.no_exclude_few_points = QtWidgets.QRadioButton(self.validation_tab)
        self.no_exclude_few_points.setObjectName("no_exclude_few_points")
        self.buttonGroup_2.addButton(self.no_exclude_few_points)
        self.gridLayout_2.addWidget(self.no_exclude_few_points, 4, 2, 1, 1)
        self.no_exclude_with_errors_rbtn = QtWidgets.QRadioButton(self.validation_tab)
        self.no_exclude_with_errors_rbtn.setObjectName("no_exclude_with_errors_rbtn")
        self.buttonGroup = QtWidgets.QButtonGroup(BatchGpsImporter)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.no_exclude_with_errors_rbtn)
        self.gridLayout_2.addWidget(self.no_exclude_with_errors_rbtn, 3, 2, 1, 1)
        self.exclude_with_errors_rbtn = QtWidgets.QRadioButton(self.validation_tab)
        self.exclude_with_errors_rbtn.setObjectName("exclude_with_errors_rbtn")
        self.buttonGroup.addButton(self.exclude_with_errors_rbtn)
        self.gridLayout_2.addWidget(self.exclude_with_errors_rbtn, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.validation_tab)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.valid_gpx_folder = QtWidgets.QLineEdit(self.validation_tab)
        self.valid_gpx_folder.setObjectName("valid_gpx_folder")
        self.gridLayout_2.addWidget(self.valid_gpx_folder, 5, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.validation_tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.extent_box = QgsExtentGroupBox(self.validation_tab)
        self.extent_box.setMaximumSize(QtCore.QSize(16777215, 150))
        self.extent_box.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.extent_box.setFlat(False)
        self.extent_box.setCheckable(True)
        self.extent_box.setChecked(False)
        self.extent_box.setProperty("collapsed", False)
        self.extent_box.setProperty("syncGroup", "")
        self.extent_box.setProperty("scrollOnExpand", False)
        self.extent_box.setProperty("saveCollapsedState", False)
        self.extent_box.setProperty("saveCheckedState", False)
        self.extent_box.setObjectName("extent_box")
        self.gridLayout_2.addWidget(self.extent_box, 2, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.validation_tab)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tab_widget.addTab(self.validation_tab, "")
        self.fields_tab = QtWidgets.QWidget()
        self.fields_tab.setObjectName("fields_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fields_tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.fields_tab)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.exclude_fields_groupbox = QtWidgets.QGroupBox(self.fields_tab)
        self.exclude_fields_groupbox.setCheckable(True)
        self.exclude_fields_groupbox.setObjectName("exclude_fields_groupbox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.exclude_fields_groupbox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exclude_fields_view = QtWidgets.QTreeView(self.exclude_fields_groupbox)
        self.exclude_fields_view.setFrameShape(QtWidgets.QFrame.Box)
        self.exclude_fields_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.exclude_fields_view.setAlternatingRowColors(False)
        self.exclude_fields_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.exclude_fields_view.setObjectName("exclude_fields_view")
        self.horizontalLayout_2.addWidget(self.exclude_fields_view)
        self.gridLayout_3.addWidget(self.exclude_fields_groupbox, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(24, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.tab_widget.addTab(self.fields_tab, "")
        self.log_tab = QtWidgets.QWidget()
        self.log_tab.setObjectName("log_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.log_tab)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.log_tab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 109, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.progress_text_edit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.progress_text_edit.setFrameShape(QtWidgets.QFrame.Box)
        self.progress_text_edit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.progress_text_edit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.progress_text_edit.setObjectName("progress_text_edit")
        self.verticalLayout_5.addWidget(self.progress_text_edit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.tab_widget.addTab(self.log_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.about_box = QtWidgets.QTextEdit(self.tab)
        self.about_box.setFrameShape(QtWidgets.QFrame.Box)
        self.about_box.setObjectName("about_box")
        self.verticalLayout_7.addWidget(self.about_box)
        self.tab_widget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tab_widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(BatchGpsImporter)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.dynamic_help_box = QtWebKitWidgets.QWebView(BatchGpsImporter)
        self.dynamic_help_box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dynamic_help_box.sizePolicy().hasHeightForWidth())
        self.dynamic_help_box.setSizePolicy(sizePolicy)
        self.dynamic_help_box.setUrl(QtCore.QUrl("about:blank"))
        self.dynamic_help_box.setRenderHints(QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.dynamic_help_box.setObjectName("dynamic_help_box")
        self.horizontalLayout.addWidget(self.dynamic_help_box)

        self.retranslateUi(BatchGpsImporter)
        self.tab_widget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(BatchGpsImporter.accept)
        self.buttonBox.rejected.connect(BatchGpsImporter.reject)
        QtCore.QMetaObject.connectSlotsByName(BatchGpsImporter)

    def retranslateUi(self, BatchGpsImporter):
        _translate = QtCore.QCoreApplication.translate
        BatchGpsImporter.setWindowTitle(_translate("BatchGpsImporter", "Batch GPS Importer"))
        self.label_6.setText(_translate("BatchGpsImporter", "Projection"))
        self.label.setText(_translate("BatchGpsImporter", "GPX folder"))
        self.route.setText(_translate("BatchGpsImporter", "Route"))
        self.input_gpx_file_btn.setText(_translate("BatchGpsImporter", "Browse..."))
        self.label_3.setText(_translate("BatchGpsImporter", "Scan sub-folders"))
        self.label_11.setText(_translate("BatchGpsImporter", "Geometry type"))
        self.no_scan_sub_folders_rbtn.setText(_translate("BatchGpsImporter", "No"))
        self.scan_sub_folders_rdb.setText(_translate("BatchGpsImporter", "Yes"))
        self.track.setText(_translate("BatchGpsImporter", "Track"))
        self.label_2.setText(_translate("BatchGpsImporter", "GPX Format"))
        self.waypoint.setText(_translate("BatchGpsImporter", "Waypoint"))
        self.label_8.setText(_translate("BatchGpsImporter", "Layer name"))
        self.prefix_label.setText(_translate("BatchGpsImporter", "File name prefix"))
        self.suffix_label.setText(_translate("BatchGpsImporter", "File name suffix"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.input_output_tab), _translate("BatchGpsImporter", "Input and Output"))
        self.label_5.setText(_translate("BatchGpsImporter", "Exclude with insufficient points"))
        self.invalid_folder_btn.setText(_translate("BatchGpsImporter", "Browse..."))
        self.valid_folder_btn.setText(_translate("BatchGpsImporter", "Browse..."))
        self.label_10.setText(_translate("BatchGpsImporter", "Invalid GPX folder"))
        self.exclude_with_few_points.setText(_translate("BatchGpsImporter", "Yes"))
        self.no_exclude_few_points.setText(_translate("BatchGpsImporter", "No"))
        self.no_exclude_with_errors_rbtn.setText(_translate("BatchGpsImporter", "No"))
        self.exclude_with_errors_rbtn.setText(_translate("BatchGpsImporter", "Yes"))
        self.label_4.setText(_translate("BatchGpsImporter", "Exclude with geometry error"))
        self.label_7.setText(_translate("BatchGpsImporter", "Valid GPX folder"))
        self.extent_box.setTitle(_translate("BatchGpsImporter", "Map extent (current: none)"))
        self.extent_box.setProperty("titleBase", _translate("BatchGpsImporter", "Map extent"))
        self.label_9.setText(_translate("BatchGpsImporter", "Exclude outside extent"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.validation_tab), _translate("BatchGpsImporter", "Validation"))
        self.label_12.setText(_translate("BatchGpsImporter", "Choose layer fields"))
        self.exclude_fields_groupbox.setTitle(_translate("BatchGpsImporter", "Check All/ Uncheck All"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.fields_tab), _translate("BatchGpsImporter", "Fields"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.log_tab), _translate("BatchGpsImporter", "Log"))
        self.about_box.setHtml(_translate("BatchGpsImporter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Batch GPS Importer</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Version 1.0.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Batch GPS Importer is a GPX file import automation plugin that converts multiple GPX files into a single layer with multiple features based on features in each gpx file. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Batch GPS Importer is developed and maintained by Wondimagegn Tesfaye Beshah. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">It is a free software under GNU General Public License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.datumhelper.com/products/batch-gps-importer\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Product Home</span></a><span style=\" font-size:8pt;\">, </span><a href=\"http://www.datumhelper.com/products/batch-gps-importer/documentation\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Documentation</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Copyright © 2017 </span><a href=\"http://www.datumhelper.com/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Wondimagegn Tesfaye Beshah</span></a><span style=\" font-size:8pt;\">. All rights reserved.</span></p></body></html>"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("BatchGpsImporter", "About"))

from PyQt5 import QtWebKitWidgets
from qgis.gui import QgsExtentGroupBox
from qgis.gui import QgsProjectionSelectionWidget
